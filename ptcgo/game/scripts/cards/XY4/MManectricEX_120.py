from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.pokemon import is_energy_card
from ptcgo.game.card_effects.support_common import attach_from_discard


def _is_benched(pokemon) -> bool:
    return not is_in_active_spot(pokemon)


def _is_basic_energy(card) -> bool:
    return (is_energy_card(card)
            and not card.get_attribute(AttrID.IS_SPECIAL_ENERGY))


card = PokemonCardDef(
    guid="5d337ad6-0d32-5af7-89cd-d36cec8e8337",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MManectricEX.Name",
    display_name="M Manectric-EX",
    searchable_by=["M Manectric-EX", "MEGA", "EX", "MManectricEX"],
    subtypes=["MEGA", "EX"],
    collector_number=120,
    set_code="XY4",
    rarity=Rarities.RareSecret,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ManectricEX.Name",
    family_id=310,
    abilities=[
        Attack(
            title="Turbo Bolt",
            game_text="Attach 2 basic Energy cards from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=attach_from_discard(_is_basic_energy, count=2, target=_is_benched),
        ),
    ],
)
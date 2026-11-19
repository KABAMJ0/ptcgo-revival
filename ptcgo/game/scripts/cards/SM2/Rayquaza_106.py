from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.passives_common import (
    is_in_active_spot,
    no_weakness_passive,
)
from ptcgo.game.card_effects.pokemon import is_energy_card
from ptcgo.game.card_effects.support_common import attach_from_discard

def _is_basic_energy(card) -> bool:
    return (is_energy_card(card)
            and not card.get_attribute(AttrID.IS_SPECIAL_ENERGY))


def _is_benched(pokemon) -> bool:
    return not is_in_active_spot(pokemon)

card = PokemonCardDef(
    guid="21a380f8-2e94-5d73-ba05-0437b7d1e237",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name",
    display_name="Rayquaza",
    searchable_by=["Rayquaza", "Basic", "Rayquaza"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=384,
    abilities=[
        Attack(
            title="Turbo Storm",
            game_text="Attach 2 basic Energy cards from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=attach_from_discard(_is_basic_energy, count=2, target=_is_benched),
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
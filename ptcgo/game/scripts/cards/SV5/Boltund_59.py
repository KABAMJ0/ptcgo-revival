from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID

_basic_lightning = lambda card: (
    is_basic_energy_card(card)
    and PokemonTypes.LIGHTNING.value in (card.get_attribute(AttrID.POKEMON_TYPES) or []))


card = PokemonCardDef(
    guid="c4c755a5-712e-5985-9717-d6c4aa1b21f2",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Boltund.Name",
    display_name="Boltund",
    searchable_by=["Boltund", "Stage 1", "Boltund"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yamper.Name",
    family_id=835,
    abilities=[
        Attack(
            title="Electrifying Dash",
            game_text="Search your deck for up to 2 Basic Lightning Energy cards and attach them to your Benched Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=search_attach_energy(_basic_lightning, count=2,
                                        target_pred=lambda p: not is_in_active_spot(p)),
        ),
    ],
)
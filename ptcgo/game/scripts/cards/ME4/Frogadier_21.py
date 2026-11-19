from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.session.effects import is_pokemon_card

card = PokemonCardDef(
    guid="a9781c1d-0f2e-5d64-b6e2-36699aeccdc8",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    display_name="Frogadier",
    searchable_by=["Frogadier", "Stage 1", "Frogadier"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="ME4",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Froakie.Name",
    family_id=656,
    abilities=[
        Attack(
            title="Summoning Jutsu",
            game_text="Search your deck for up to 3 Pok\u00e9mon, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=search_to_hand(is_pokemon_card, count=3, reveal=True),
        ),
        Attack(
            title="Aqua Edge",
            cost={PokemonTypes.WATER: 2},
            damage=50,
        ),
    ],
)
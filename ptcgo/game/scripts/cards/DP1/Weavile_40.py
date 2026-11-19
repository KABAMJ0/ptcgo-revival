from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="d1bf6e84-60ee-527e-b27e-e9263d2e2e01",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weavile.Name",
    display_name="Weavile",
    searchable_by=["Weavile", "Stage 1", "Weavile"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="DP1",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    family_id=215,
    abilities=[
        Attack(
            title="Nasty Plot",
            game_text="Search your deck for any 1 card and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=search_to_hand(None, count=1, minimum=1, reveal=False),
        ),
        Attack(
            title="Dark Pulse",
            game_text="Does 10 damage times the total amount of Darkness Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)
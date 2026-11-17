from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cc6d8d36-618c-54c4-82fd-0d3fc9a4f35f",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arbokex.Name",
    display_name="Arbok ex",
    searchable_by=["Arbok ex", "Stage 1", "ex", "Arbokex"],
    subtypes=["Stage 1", "ex"],
    collector_number=24,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name",
    family_id=23,
    abilities=[
        Attack(
            title="Bind Down",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=70,
            effect=unimplemented,
        ),
        Attack(
            title="Menacing Fangs",
            game_text="Your opponent discards 2 cards from their hand.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=150,
            effect=unimplemented,
        ),
    ],
)
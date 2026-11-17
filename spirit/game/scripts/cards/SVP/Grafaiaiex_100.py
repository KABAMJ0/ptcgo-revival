from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="75e856a7-d338-5a6d-9b98-5fdd62b1e187",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grafaiaiex.Name",
    display_name="Grafaiai ex",
    searchable_by=["Grafaiai ex", "Stage 1", "ex", "Grafaiaiex"],
    subtypes=["Stage 1", "ex"],
    collector_number=100,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shroodle.Name",
    family_id=944,
    abilities=[
        Attack(
            title="Numbing Saliva",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Toxic Throw",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. During your next turn, this Pok\u00e9mon can't use Toxic Throw.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=unimplemented,
        ),
    ],
)
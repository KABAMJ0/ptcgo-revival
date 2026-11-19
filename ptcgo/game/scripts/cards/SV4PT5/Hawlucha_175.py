from ptcgo.game.card_effects.attacks_common import bench_counter_picks
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="25eecc4e-3655-5ffe-a7d2-091518e72944",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hawlucha.Name",
    display_name="Hawlucha",
    searchable_by=["Hawlucha", "Basic", "Hawlucha"],
    subtypes=["Basic"],
    collector_number=175,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=701,
    abilities=[
        Ability(
            title="Flying Entry",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may choose 2 of your opponent's Benched Pok\u00e9mon and put 1 damage counter on each of them.",
            trigger=Triggers.ON_PLAY,
            effect=bench_counter_picks(picks=2, each=1),
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
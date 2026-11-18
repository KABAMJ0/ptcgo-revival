from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dbcff7c1-4501-5602-8fed-a0d160f783bd",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blissey.Name",
    display_name="Blissey",
    searchable_by=["Blissey", "Stage 1", "Blissey"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    family_id=113,
    abilities=[
        Ability(
            title="Happy Healing",
            game_text="Once during your turn (before your attack), choose 1 of your Benched Pok\u00e9mon and flip a coin. If heads, count the number of Energy attached to Blissey and then remove that many damage counters from the chosen Benched Pok\u00e9mon. This power can't be used if Blissey is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Smash Bomber",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=unimplemented,
        ),
    ],
)
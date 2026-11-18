from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1e5d891a-039c-5cec-b368-17d5d7a988a0",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cradily.Name",
    display_name="Cradily",
    searchable_by=["Cradily", "Stage 2", "Cradily"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name",
    family_id=345,
    abilities=[
        Ability(
            title="Selective Slime",
            game_text="Once during your turn, you may flip a coin. If heads, choose Burned, Confused, or Poisoned. Your opponent's Active Pok\u00e9mon is now affected by that Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Miasma Wind",
            game_text="This attack does 100 damage for each Special Condition affecting your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=100,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)
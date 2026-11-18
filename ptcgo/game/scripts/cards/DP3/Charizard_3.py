from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="efa3f6be-164c-5c6b-a20b-c630ec2a8471",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="DP3",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Ability(
            title="Fury Blaze",
            game_text="If your opponent has 3 or less Prize cards left, each of Charizard's attacks does 50 more damage to the Active Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Blast Burn",
            game_text="Flip a coin. If heads, discard 2 Energy cards attached to Charizard. If tails, discard 4 Energy cards attached to Charizard. (If you can't, this attack does nothing.)",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="62fcedd8-2c82-53a6-9344-9e20797b291f",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizardex.Name",
    display_name="Charizard ex",
    searchable_by=["Charizard ex", "Stage 2", "ex", "Charizardex"],
    subtypes=["Stage 2", "ex"],
    collector_number=105,
    set_code="EX6",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Ability(
            title="Energy Flame",
            game_text="All Energy attached to Charizard ex are Fire Energy instead of its usual type.",
            effect=unimplemented,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
        Attack(
            title="Burn Down",
            game_text="Discard 5 Fire Energy attached to Charizard ex. This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, and any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 5},
            damage=200,
            effect=unimplemented,
        ),
    ],
)
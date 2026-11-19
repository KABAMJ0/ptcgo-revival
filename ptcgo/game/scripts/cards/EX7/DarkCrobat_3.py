from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cdb480b2-5ac9-53be-8699-a91074a2a487",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkCrobat.Name",
    display_name="Dark Crobat",
    searchable_by=["Dark Crobat", "Stage 2", "DarkCrobat"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkGolbat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Black Beam",
            game_text="Once during your turn (before your attack), if Dark Crobat is your Active Pok\u00e9mon, you may choose 1 of the Defending Pok\u00e9mon. That Pok\u00e9mon is now Poisoned. This power can't be used if Dark Crobat is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Dark Drain",
            game_text="Does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Remove from Dark Crobat a number of damage counters equal to the number of your opponent's Pok\u00e9mon in play.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Skill Dive",
            game_text="Does 30 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)
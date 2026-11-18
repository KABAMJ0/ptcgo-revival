from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="892b4939-77ca-5b5c-a87b-a8f65278737c",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name",
    display_name="Metagross",
    searchable_by=["Metagross", "Stage 2", "Metagross"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="PL3",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Ability(
            title="Gravitation",
            game_text="Each Pok\u00e9mon in play (both yours and your opponent's) gets -20 HP. No more than 20 HP can be reduced by all Gravitation Pok\u00e9-Bodies.",
            effect=unimplemented,
        ),
        Attack(
            title="Geo Impact",
            game_text="If you have a Stadium card in play, this attack does 20 damage to each of your opponent's Benched Pok\u00e9mon that is the same type as the Defending Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
    ],
)
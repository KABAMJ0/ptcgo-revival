from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f4529225-2b26-559e-88b0-3e6be5ea44f5",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blaziken.Name",
    display_name="Blaziken",
    searchable_by=["Blaziken", "Stage 2", "Blaziken"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="PL1",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    family_id=255,
    abilities=[
        Ability(
            title="Fire Breath",
            game_text="Once during your turn (before your attack), you may choose 1 of the Defending Pok\u00e9mon. That Pok\u00e9mon is now Burned. This power can't be used if Blaziken is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Clutch",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Fire Spin",
            game_text="Discard 2 Energy attached to Blaziken.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)
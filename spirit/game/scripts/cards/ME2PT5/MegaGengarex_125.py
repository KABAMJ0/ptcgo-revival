from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="528a92b1-2b7b-57a3-a781-27d599f68042",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaGengarex.Name",
    display_name="Mega Gengar ex",
    searchable_by=["Mega Gengar ex", "Stage 2", "MEGA", "ex", "MegaGengarex"],
    subtypes=["Stage 2", "MEGA", "ex"],
    collector_number=125,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=350,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Shadowy Concealment",
            game_text="If 1 of your Darkness Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon ex, that player takes 1 fewer Prize card. The effect of Shadowy Concealment doesn't stack.",
            effect=unimplemented,
        ),
        Attack(
            title="Void Gale",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=230,
            effect=unimplemented,
        ),
    ],
)
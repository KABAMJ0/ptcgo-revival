from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3e580459-9f8f-50aa-8b70-8b498741dd9d",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Munkidoriex.Name",
    display_name="Munkidori ex",
    searchable_by=["Munkidori ex", "Basic", "ex", "Munkidoriex"],
    subtypes=["Basic", "ex"],
    collector_number=83,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Ability(
            title="Oh No You Don't",
            game_text="If this Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, and if you have any Pecharunt ex in play, your opponent takes 1 fewer Prize card.",
            effect=unimplemented,
        ),
        Attack(
            title="Dirty Headbutt",
            game_text="During your next turn, this Pok\u00e9mon can't use Dirty Headbutt.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=unimplemented,
        ),
    ],
)
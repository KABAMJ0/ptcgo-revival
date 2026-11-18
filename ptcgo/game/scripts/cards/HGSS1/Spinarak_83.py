from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9badf67a-0551-54be-971d-faa62e67e2fe",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    display_name="Spinarak",
    searchable_by=["Spinarak", "Basic", "Spinarak"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="HGSS1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=167,
    abilities=[
        Attack(
            title="Hang Down",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Spider Web",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
    ],
)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="42441248-8192-5271-90f7-89bacb66c09f",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name",
    display_name="Lileep",
    searchable_by=["Lileep", "Stage 1", "Lileep"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="SV7",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AntiqueRootFossil.Name",
    family_id=345,
    abilities=[
        Attack(
            title="Bind Down",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)
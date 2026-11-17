from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="342b311b-08a6-546e-bb89-2dcc8a10faac",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Boldore.Name",
    display_name="Boldore",
    searchable_by=["Boldore", "Stage 1", "Boldore"],
    subtypes=["Stage 1"],
    collector_number=128,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Roggenrola.Name",
    family_id=524,
    abilities=[
        Attack(
            title="Smack Down",
            game_text="If your opponent's Active Pok\u00e9mon has Fighting Resistance, this attack does 50 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Power Gem",
            cost={PokemonTypes.FIGHTING: 3},
            damage=90,
        ),
    ],
)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ab45be4a-dc66-5ec3-945e-8f51b5b3bbbc",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cloyster.Name",
    display_name="Cloyster",
    searchable_by=["Cloyster", "Stage 1", "Cloyster"],
    subtypes=["Stage 1"],
    collector_number=91,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shellder.Name",
    family_id=90,
    abilities=[
        Attack(
            title="Protect Charge",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 80 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 2},
            damage=80,
            effect=unimplemented,
        ),
    ],
)
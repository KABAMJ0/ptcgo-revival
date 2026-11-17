from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="769c79c2-87cd-51fc-9ded-bd089be5e159",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garganacl.Name",
    display_name="Garganacl",
    searchable_by=["Garganacl", "Stage 2", "Garganacl"],
    subtypes=["Stage 2"],
    collector_number=84,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Naclstack.Name",
    family_id=932,
    abilities=[
        Ability(
            title="Powerful a-Salt",
            game_text="Attacks used by your Fighting Pok\u00e9mon do 30 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
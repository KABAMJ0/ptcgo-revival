from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2e9621af-4833-5697-afc9-927a4b5581d6",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garganacl.Name",
    display_name="Garganacl",
    searchable_by=["Garganacl", "Stage 2", "Garganacl"],
    subtypes=["Stage 2"],
    collector_number=178,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Naclstack.Name",
    family_id=932,
    abilities=[
        Ability(
            title="Blessed Salt",
            game_text="During Pok\u00e9mon Checkup, heal 20 damage from each of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Knocking Hammer",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=130,
            effect=unimplemented,
        ),
    ],
)
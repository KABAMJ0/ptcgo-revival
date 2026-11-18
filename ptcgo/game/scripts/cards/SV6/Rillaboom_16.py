from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="50971bb7-1e0f-50be-8809-a5b9957cfaab",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rillaboom.Name",
    display_name="Rillaboom",
    searchable_by=["Rillaboom", "Stage 2", "Rillaboom"],
    subtypes=["Stage 2"],
    collector_number=16,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Thwackey.Name",
    family_id=810,
    abilities=[
        Attack(
            title="Drum Beating",
            game_text="During your opponent's next turn, attacks used by the Defending Pok\u00e9mon cost Colorless more, and its Retreat Cost is Colorless more.",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Wood Hammer",
            game_text="This Pok\u00e9mon also does 50 damage to itself.",
            cost={PokemonTypes.GRASS: 2},
            damage=180,
            effect=unimplemented,
        ),
    ],
)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="888062bf-923f-5b4d-b270-1d90aefddc83",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name",
    display_name="Magnezone",
    searchable_by=["Magnezone", "Stage 2", "Magnezone"],
    subtypes=["Stage 2"],
    collector_number=47,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    family_id=81,
    abilities=[
        Attack(
            title="Upper Spark",
            game_text="If this Pok\u00e9mon evolved from Magneton during this turn, this attack does 120 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Flashing Bolt",
            game_text="During your next turn, this Pok\u00e9mon can't use Flashing Bolt.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=160,
            effect=unimplemented,
        ),
    ],
)
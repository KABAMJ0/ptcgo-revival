from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="405b0555-30f1-5ad8-9bee-31c5fd1ceeca",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanilluxe.Name",
    display_name="Vanilluxe",
    searchable_by=["Vanilluxe", "Stage 2", "Vanilluxe"],
    subtypes=["Stage 2"],
    collector_number=45,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name",
    family_id=582,
    abilities=[
        Ability(
            title="Frigid Room",
            game_text="Your opponent's Pok\u00e9mon that have 40 HP or less remaining can't attack.",
            effect=unimplemented,
        ),
        Attack(
            title="Icicle Missile",
            cost={PokemonTypes.WATER: 2},
            damage=110,
        ),
    ],
)
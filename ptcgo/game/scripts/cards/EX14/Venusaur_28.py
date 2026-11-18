from ptcgo.game.card_effects.passives_common import rewrite_energy_types_passive
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="deb6e18d-b95f-5f6e-bbdc-4ad363e79a70",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venusaur.Name",
    display_name="Venusaur",
    searchable_by=["Venusaur", "Stage 2", "Venusaur"],
    subtypes=["Stage 2"],
    collector_number=28,
    set_code="EX14",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    family_id=1,
    abilities=[
        Ability(
            title="Chlorophyll",
            game_text="All Energy cards that provide only Colorless Energy attached to your Grass Pok\u00e9mon provide Grass Energy instead.",
            passive=rewrite_energy_types_passive(PokemonTypes.GRASS.value, protects="team", colorless_only=True, holder_types=[PokemonTypes.GRASS.value]),
        ),
        Attack(
            title="Green Blast",
            game_text="Does 20 damage plus 10 more damage for each Grass Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Toxic Sleep",
            game_text="The Defending Pok\u00e9mon is now Asleep and Poisoned. Put 2 damage counters instead of 1 on the Defending Pok\u00e9mon between turns.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)
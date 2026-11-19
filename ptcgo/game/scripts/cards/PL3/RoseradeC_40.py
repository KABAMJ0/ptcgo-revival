from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import cure_on_energy_attach

card = PokemonCardDef(
    guid="86db8a10-3e5d-5873-97db-465b0be552f1",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RoseradeC.Name",
    display_name="Roserade C",
    searchable_by=["Roserade C", "Basic", "SP", "RoseradeC"],
    subtypes=["Basic", "SP"],
    collector_number=40,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=407,
    abilities=[
        Ability(
            title="Natural Cure",
            game_text="When you attach an Energy card from your hand to Roserade C, remove all Special Conditions from Roserade C.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=cure_on_energy_attach(),
        ),
        Attack(
            title="Magical Leaf",
            game_text="Flip a coin. If heads, this attack does 40 damage plus 20 more damage and remove 2 damage counters from Roserade C.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
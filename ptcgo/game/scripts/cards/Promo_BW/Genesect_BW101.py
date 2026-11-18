from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0446bd2e-f377-559c-a9aa-21f15dbc8e81",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Genesect.Name",
    display_name="Genesect",
    searchable_by=["Genesect", "Basic", "Genesect"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=649,
    abilities=[
        Attack(
            title="Hyper Beam",
            game_text="Flip a coin. If heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Breaker Bazooka",
            game_text="Discard all Grass Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=self_energy_discard_attack(all_energy=True, energy_type=PokemonTypes.GRASS),
        ),
    ],
)
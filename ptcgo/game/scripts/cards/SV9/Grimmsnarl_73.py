from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_per, defender_retreat_cost
card = PokemonCardDef(
    guid="eebaad6d-8207-5294-b932-49b43aa632ac",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grimmsnarl.Name",
    display_name="Grimmsnarl",
    searchable_by=["Grimmsnarl", "Stage 2", "Grimmsnarl"],
    subtypes=["Stage 2"],
    collector_number=73,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Morgrem.Name",
    family_id=859,
    abilities=[
        Attack(
            title="Shadowy Knot",
            game_text="This attack does 50 damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=50,
            damage_operator="x",
            effect=damage_per(defender_retreat_cost, 50),
        ),
        Attack(
            title="Mega Punch",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
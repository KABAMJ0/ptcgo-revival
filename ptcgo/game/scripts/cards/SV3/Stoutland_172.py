from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_per, defender_retreat_cost
card = PokemonCardDef(
    guid="16dcf8ec-f180-5240-af91-f20914d5e64e",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stoutland.Name",
    display_name="Stoutland",
    searchable_by=["Stoutland", "Stage 2", "Stoutland"],
    subtypes=["Stage 2"],
    collector_number=172,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name",
    family_id=506,
    abilities=[
        Attack(
            title="Chomp Chomp Panic",
            game_text="This attack does 50 damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=damage_per(defender_retreat_cost, 50),
        ),
        Attack(
            title="Sharp Fang",
            cost={PokemonTypes.COLORLESS: 3},
            damage=140,
        ),
    ],
)
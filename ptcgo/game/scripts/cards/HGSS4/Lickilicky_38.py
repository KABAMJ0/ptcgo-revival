from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import count_energy, damage_counters_on, snipe_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4d1e5979-e6b1-5285-a0a3-c5b5f993b29d",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lickilicky.Name",
    display_name="Lickilicky",
    searchable_by=["Lickilicky", "Stage 1", "Lickilicky"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="HGSS4",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name",
    family_id=108,
    abilities=[
        Attack(
            title="Licking Shot",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 10 damage to that Pok\u00e9mon for each Energy attached to Lickilicky. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(
                lambda ctx: 10 * count_energy("self")(ctx),
                pool="any", count=1, apply_modifiers=False,
            ),
        ),
        Attack(
            title="Stick and Absorb",
            game_text="Remove 2 damage counters from Lickilicky. The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=unimplemented,
        ),
    ],
)
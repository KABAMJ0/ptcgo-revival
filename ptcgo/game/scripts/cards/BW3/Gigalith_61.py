from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import count_energy, damage_counters_on, snipe_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4ff358ff-cb75-59f3-996d-026b00e7be33",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gigalith.Name",
    display_name="Gigalith",
    searchable_by=["Gigalith", "Stage 2", "Gigalith"],
    subtypes=["Stage 2"],
    collector_number=61,
    set_code="BW3",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Boldore.Name",
    family_id=526,
    abilities=[
        Attack(
            title="Core Cannon",
            game_text="This attack does 20 damage to 1 of your opponent's Pok\u00e9mon for each Fighting Energy attached to this Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            effect=snipe_attack(
                lambda ctx: 20 * count_energy("self", energy_type=PokemonTypes.FIGHTING)(ctx),
                pool="any", count=1, apply_modifiers=False,
            ),
        ),
        Attack(
            title="Power Gem",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)
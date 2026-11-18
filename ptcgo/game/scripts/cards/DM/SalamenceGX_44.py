from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(
    guid="829ef99a-040d-580c-96c3-594ed9a99c3f",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SalamenceGX.Name",
    display_name="Salamence-GX",
    searchable_by=["Salamence-GX", "Stage 2", "GX", "SalamenceGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=44,
    set_code="DM",
    rarity=Rarities.RareHolo,
    hp=250,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    family_id=371,
    abilities=[
        Ability(
            title="Dragon Lift",
            game_text="Your Pok\u00e9mon in play have no Retreat Cost, except Pok\u00e9mon-GX and Pok\u00e9mon-EX.",
            effect=unimplemented,
        ),
        Attack(
            title="Bright Flame",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=self_energy_discard_attack(count=2),
        ),
        Attack(
            title="Flame Jet-GX",
            game_text="This attack does 120 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)
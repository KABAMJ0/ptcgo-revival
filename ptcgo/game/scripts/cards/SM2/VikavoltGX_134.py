from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack, spread_damage

card = PokemonCardDef(
    guid="656b0d9a-70b8-5e2b-a96c-0d761c275319",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VikavoltGX.Name",
    display_name="Vikavolt-GX",
    searchable_by=["Vikavolt-GX", "Stage 2", "GX", "VikavoltGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=134,
    set_code="SM2",
    rarity=Rarities.RareUltra,
    hp=240,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name",
    family_id=738,
    abilities=[
        Attack(
            title="Charge Beam",
            game_text="Attach an Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Super Zap Cannon",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=self_energy_discard_attack(count=2),
        ),
        Attack(
            title="Gigatron-GX",
            game_text="This attack does 60 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            effect=spread_damage(60, side="opponent"),
        ),
    ],
)
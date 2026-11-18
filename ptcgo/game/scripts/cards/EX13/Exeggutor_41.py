from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="16a5a1a0-5d16-5e91-81d3-123424ee6484",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggutor.Name",
    display_name="Exeggutor δ",
    searchable_by=["Exeggutor \u03b4", "Stage 1", "Exeggutor"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="EX13",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=103,
    abilities=[
        Attack(
            title="Delta Circle",
            game_text="Does 10 damage plus 10 more damage for each Pok\u00e9mon you have in play that has \u03b4 on its card.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Split Bomb",
            game_text="Choose 2 of your opponent's Pok\u00e9mon. This attack does 30 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            effect=snipe_attack(30, pool="any", count=2, apply_modifiers=False),
        ),
    ],
)
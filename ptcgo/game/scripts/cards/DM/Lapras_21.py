from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per


card = PokemonCardDef(
    guid="d82eb6fb-ea70-5a1f-b893-d6dc299a43fe",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name",
    display_name="Lapras",
    searchable_by=["Lapras", "Basic", "Lapras"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="DM",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=131,
    abilities=[
        Attack(
            title="Aqua Bullet",
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=snipe_attack(20, pool="bench", count=1, apply_modifiers=False),
        ),
        Attack(
            title="Hydro Pump",
            game_text="This attack does 10 more damage times the amount of Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            effect=damage_per(count_energy('self', energy_type=PokemonTypes.WATER), 10, base=70),
        ),
    ],
)
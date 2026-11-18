from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="09724ee4-c80a-56ec-bd4e-046738ccc7cd",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glaceonex.Name",
    display_name="Glaceon ex",
    searchable_by=["Glaceon ex", "Stage 1", "Tera", "ex", "Glaceonex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=150,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Frost Bullet",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=snipe_attack(30, pool="bench", count=1, apply_modifiers=False, also_base=True),
        ),
        Attack(
            title="Euclase",
            game_text="Knock Out 1 of your opponent's Pok\u00e9mon that has exactly 6 damage counters on it.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1, PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
    ],
)
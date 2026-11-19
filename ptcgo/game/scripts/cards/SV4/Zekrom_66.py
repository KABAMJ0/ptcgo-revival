from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.card_effects.attacks_common import snipe_attack, discard_defender_tools_then_damage
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f33b1c0d-0d99-510a-8230-e2d4c21dba7b",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zekrom.Name",
    display_name="Zekrom",
    searchable_by=["Zekrom", "Basic", "Zekrom"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=644,
    abilities=[
        Attack(
            title="Crushing Short",
            game_text="Before doing damage, discard all Pok\u00e9mon Tools from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=discard_defender_tools_then_damage(),
        ),
        Attack(
            title="Raging Thunder",
            game_text="This attack also does 40 damage to 1 of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=snipe_attack(40, pool="bench", side="mine", also_base=True),
        ),
    ],
)
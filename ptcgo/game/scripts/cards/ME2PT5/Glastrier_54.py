from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="8e5a3f3d-ea18-53f8-8edb-339cf01a8c45",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glastrier.Name",
    display_name="Glastrier",
    searchable_by=["Glastrier", "Basic", "Glastrier"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=896,
    abilities=[
        Attack(
            title="Ice Shot",
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=snipe_attack(20, pool="bench", also_base=True, apply_modifiers=False),
        ),
        Attack(
            title="Frosty Typhoon",
            game_text="During your next turn, this Pok\u00e9mon can't use Frosty Typhoon.",
            cost={PokemonTypes.WATER: 3},
            damage=130,
            effect=unimplemented,
        ),
    ],
)
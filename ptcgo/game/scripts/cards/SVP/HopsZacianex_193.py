from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ceeb9a03-916e-5dec-8f16-b8e130da05a4",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsZacianex.Name",
    display_name="Hop's Zacian ex",
    searchable_by=["Hop's Zacian ex", "Basic", "ex", "HopsZacianex"],
    subtypes=["Basic", "ex"],
    collector_number=193,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=230,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=888,
    abilities=[
        Attack(
            title="Insta-Strike",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=snipe_attack(30, pool="bench", count=1, apply_modifiers=False, also_base=True),
        ),
        Attack(
            title="Brave Slash",
            game_text="During your next turn, this Pok\u00e9mon can't use Brave Slash.",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=240,
            effect=unimplemented,
        ),
    ],
)
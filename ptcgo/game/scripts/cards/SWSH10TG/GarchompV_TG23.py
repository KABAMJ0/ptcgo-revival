from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="4c368823-d862-51eb-addf-bedb73b4d18b",
    key="SWSH10TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompV.Name",
    display_name="Garchomp V",
    searchable_by=["Garchomp V", "Basic", "V", "GarchompV"],
    subtypes=["Basic", "V"],
    collector_number=23,
    set_code="SWSH10TG",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=445,
    abilities=[
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
        Attack(
            title="Sonic Strike",
            game_text="Discard 3 Energy from this Pok\u00e9mon. This attack does 220 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(220, pool="any", count=1, apply_modifiers=False),
        ),
    ],
)
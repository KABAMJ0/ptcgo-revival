from ptcgo.game.card_effects.attacks_common import mill_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2c01705c-81c8-50d1-bcd9-54f52fdda6b1",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WoChien.Name",
    display_name="Wo-Chien",
    searchable_by=["Wo-Chien", "Basic", "WoChien"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=1001,
    abilities=[
        Attack(
            title="Hazardous Greed",
            game_text="If there are 3 or fewer cards in your deck, this attack also does 120 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=mill_attack(3, opponent=False),
        ),
        Attack(
            title="Entangling Whip",
            game_text="Discard the top 3 cards of your deck.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)
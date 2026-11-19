from ptcgo.game.card_effects.attacks_common import mill_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0c1dc4c8-1b57-5eca-bd03-32a2a2e04d8a",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sizzlipede.Name",
    display_name="Sizzlipede",
    searchable_by=["Sizzlipede", "Basic", "Sizzlipede"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="ME5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=850,
    abilities=[
        Attack(
            title="Controlled Burn",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=mill_attack(1),
        ),
        Attack(
            title="Bug Out",
            game_text="Reveal the bottom 7 cards of your deck, and this attack does 50 damage for each Pok\u00e9mon you find there that has the Bug Out attack. Then, shuffle any revealed Pok\u00e9mon back into your deck. Discard the other cards.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)
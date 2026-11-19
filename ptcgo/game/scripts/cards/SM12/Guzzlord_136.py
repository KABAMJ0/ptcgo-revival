from ptcgo.game.card_effects.attacks_common import mill_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="41b09ef6-6017-5bc3-a904-82be31337a0d",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Guzzlord.Name",
    display_name="Guzzlord",
    searchable_by=["Guzzlord", "Basic", "Ultra Beast", "Guzzlord"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=136,
    set_code="SM12",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=799,
    abilities=[
        Attack(
            title="Mountain Munch",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=mill_attack(1),
        ),
        Attack(
            title="Red Banquet",
            game_text="If your opponent's Pok\u00e9mon is Knocked Out by damage from this attack, take 1 more Prize card.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)
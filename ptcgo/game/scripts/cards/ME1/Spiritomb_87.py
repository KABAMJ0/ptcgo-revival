from ptcgo.game.card_effects.attacks_common import mill_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3d412a02-a6f7-53d5-acd4-970e747fdb4e",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=442,
    abilities=[
        Ability(
            title="Spiteful Swirl",
            game_text="If your Active Darkness Pok\u00e9mon is damaged by an attack from your opponent's Pok\u00e9mon (even if your Active Darkness Pok\u00e9mon is Knocked Out), place 1 damage counter on the Attacking Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Mountain Breaker",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=mill_attack(1),
        ),
    ],
)
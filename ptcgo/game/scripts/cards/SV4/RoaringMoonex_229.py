from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_stadium_attack

card = PokemonCardDef(
    guid="24215155-e9e7-588a-9879-2318c9ed0ed1",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RoaringMoonex.Name",
    display_name="Roaring Moon ex",
    searchable_by=["Roaring Moon ex", "Basic", "ex", "Ancient", "RoaringMoonex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=229,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=1005,
    abilities=[
        Attack(
            title="Frenzied Gouging",
            game_text="Knock Out your opponent's Active Pok\u00e9mon. If your opponent's Active Pok\u00e9mon is Knocked Out in this way, this Pok\u00e9mon does 200 damage to itself.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Calamity Storm",
            game_text="You may discard a Stadium in play. If you do, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=discard_stadium_attack(optional=True, bonus=120),
        ),
    ],
)
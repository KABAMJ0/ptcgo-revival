from ptcgo.game.card_effects.attacks_common import mill_then_attach_energy
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e5256cca-5077-5f7c-905a-76cabbcda0ee",
    key="ME55C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaEX.Name",
    display_name="Rayquaza-EX",
    searchable_by=["Rayquaza-EX", "Basic", "EX", "RayquazaEX"],
    subtypes=["Basic", "EX"],
    collector_number=85,
    set_code="ME55C",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    family_id=384,
    abilities=[
        Attack(
            title="Celestial Roar",
            game_text="Discard the top 3 cards of your deck. If any of those cards are Energy cards, attach them to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Burst",
            game_text="Discard all basic Fire Energy or all basic Lightning Energy attached to this Pok\u00e9mon. This attack does 60 damage times the number of Energy cards you discarded.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)
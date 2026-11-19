from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="99603f1a-99be-53fa-b69c-bc3107f48cef",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Granbull.Name",
    display_name="Granbull",
    searchable_by=["Granbull", "Stage 1", "Granbull"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snubbull.Name",
    family_id=209,
    abilities=[
        Ability(
            title="Intimidating Fang",
            game_text="As long as Granbull is your Active Pok\u00e9mon, any damage done by an opponent's attack is reduced by 10 (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Crushing Blow",
            game_text="Flip a coin. If heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Double Lariat",
            game_text="Flip 2 coins. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=50,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=50),
        ),
    ],
)
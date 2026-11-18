from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.attacks_common import mill_scaled_damage
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="efa066c2-52c0-5460-83c5-a4ccd257f956",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesMagmar.Name",
    display_name="Blaine's Magmar",
    searchable_by=["Blaine's Magmar", "Basic", "BlainesMagmar"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=126,
    abilities=[
        Attack(
            title="Firebreathing",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage; if tails, this attack does 10 damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Lava Burst",
            game_text="Discard the top 5 cards of your deck. (If there are fewer than 5 cards in your deck, discard all of them.) This attack does 20 damage for each Fire Energy card you discarded in this way.",
            cost={PokemonTypes.FIRE: 3},
            damage=20,
            damage_operator="x",
            effect=mill_scaled_damage(
                5, 20,
                pred=lambda card: energy_provides_type(
                    card, PokemonTypes.FIRE.value
                ),
            ),
        ),
    ],
)
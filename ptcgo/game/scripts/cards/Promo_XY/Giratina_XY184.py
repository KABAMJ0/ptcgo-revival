from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_random_hand_attack

card = PokemonCardDef(
    guid="34c29038-3972-54d1-99d0-c44a1c2258e2",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Giratina.Name",
    display_name="Giratina",
    searchable_by=["Giratina", "Basic", "Giratina"],
    subtypes=["Basic"],
    collector_number=184,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=487,
    abilities=[
        Ability(
            title="Devour Light",
            game_text="Each Pok\u00e9mon BREAK has no Abilities (this includes Abilities of its previous Evolution).",
            effect=unimplemented,
        ),
        Attack(
            title="Shadow Claw",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=discard_random_hand_attack(count=1),
        ),
    ],
)
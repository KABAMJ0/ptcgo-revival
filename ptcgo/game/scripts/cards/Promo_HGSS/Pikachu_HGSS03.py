from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.card_effects.pokemon import is_lightning_energy
from ptcgo.game.card_effects.support_common import search_attach_energy


from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="15e3be52-7284-5f2e-85ba-65d610fa11c9",
    key="Promo_HGSS",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="Promo_HGSS",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=25,
    abilities=[
        Attack(
            title="Recharge",
            game_text="Flip a coin. If heads, search your deck for a Lightning Energy card and attach it to Pikachu. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_gate(search_attach_energy(is_lightning_energy,
                                                 count=1, to_self=True)),
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy attached to Pikachu.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=unimplemented,
        ),
    ],
)
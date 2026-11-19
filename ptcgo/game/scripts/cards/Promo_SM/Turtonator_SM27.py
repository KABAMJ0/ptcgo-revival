from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type, is_energy_card
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.pokemon import is_fire_energy


card = PokemonCardDef(
    guid="5a028157-0999-54ec-9dde-508ac86ea58c",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtonator.Name",
    display_name="Turtonator",
    searchable_by=["Turtonator", "Basic", "Turtonator"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=776,
    abilities=[
        Attack(
            title="Flame Cloak",
            game_text="Attach a Fire Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=attach_from_discard(is_fire_energy, count=1),
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1c3c3b37-48bf-5710-9236-5e0bf0de430e",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SilvallyGX.Name",
    display_name="Silvally-GX",
    searchable_by=["Silvally-GX", "Stage 1", "GX", "SilvallyGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=116,
    set_code="SM5",
    rarity=Rarities.RareHolo,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name",
    family_id=772,
    abilities=[
        Ability(
            title="Gyro Unit",
            game_text="Your Basic Pok\u00e9mon in play have no Retreat Cost.",
            effect=attach_from_discard(is_basic_energy_card, count=1, target="choice"),
        ),
        Attack(
            title="Turbo Drive",
            game_text="Attach a basic Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=unimplemented,
        ),
        Attack(
            title="Rebel-GX",
            game_text="This attack does 50 damage for each of your opponent's Benched Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)